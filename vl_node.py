import requests
from PIL import Image
from io import BytesIO
import numpy as np
import torch
import base64
import json

class VL_QwenDescribeImage:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
            },
            "optional": {
                "api_url": ("STRING", {
                    "default": "https://api.siliconflow.cn/v1",
                    "multiline": False,
                    "tooltip": "API服务器地址"
                }),
                "model": ("STRING", {
                    "default": "Qwen/Qwen2.5-VL-72B-Instruct",
                    "multiline": False,
                    "tooltip": "使用的视觉语言模型"
                }),
                "prompt": ("STRING", {
                    "default": "请描述这张图片的内容。",
                    "multiline": True,
                    "tooltip": "给模型的提示词，描述你希望模型如何分析图片"
                }),
                "api_key": ("STRING", {
                    "default": "",
                    "multiline": False,
                    "tooltip": "API密钥，如果需要认证请填入"
                }),
                "timeout": ("INT", {
                    "default": 60,
                    "min": 10,
                    "max": 300,
                    "step": 10,
                    "tooltip": "请求超时时间（秒）"
                }),
                "max_tokens": ("INT", {
                    "default": 1000,
                    "min": 100,
                    "max": 4000,
                    "step": 100,
                    "tooltip": "最大返回token数量"
                }),
                "temperature": ("FLOAT", {
                    "default": 0.7,
                    "min": 0.0,
                    "max": 2.0,
                    "step": 0.1,
                    "tooltip": "生成文本的随机性，0为最确定，2为最随机"
                }),
                "image_quality": ("INT", {
                    "default": 95,
                    "min": 50,
                    "max": 100,
                    "step": 5,
                    "tooltip": "上传图片的JPEG质量"
                }),
                "detail": (["auto", "low", "high"], {
                    "default": "auto",
                    "tooltip": "图像处理详细程度：auto=自动选择，low=低分辨率快速处理，high=高分辨率详细分析"
                }),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("description",)
    FUNCTION = "describe"
    CATEGORY = "VL Model"
    
    def describe(self, image, api_url="https://api.siliconflow.cn/v1", model="Qwen/Qwen2.5-VL-72B-Instruct", 
                 prompt="请描述这张图片的内容。", api_key="", timeout=60, max_tokens=1000, 
                 temperature=0.7, image_quality=95, detail="auto"):
        try:
            # 处理ComfyUI的图像格式 (batch, height, width, channels)
            if isinstance(image, torch.Tensor):
                img_array = image[0].cpu().numpy()
                img_array = (img_array * 255).astype(np.uint8)
            else:
                img_array = image[0] if len(image.shape) == 4 else image
                img_array = (img_array * 255).astype(np.uint8) if img_array.max() <= 1.0 else img_array.astype(np.uint8)
            
            # 转换为PIL Image
            img = Image.fromarray(img_array)
            
            # 将图片编码为base64
            buffered = BytesIO()
            img.save(buffered, format="JPEG", quality=image_quality)
            img_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
            
            # 准备OpenAI风格的请求头
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json"
            }
            if api_key and api_key.strip():
                headers["Authorization"] = f"Bearer {api_key.strip()}"
            
            # 准备OpenAI风格的请求体
            payload = {
                "model": model,
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": prompt
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{img_base64}",
                                    "detail": detail
                                }
                            }
                        ]
                    }
                ],
                "max_tokens": max_tokens,
                "temperature": temperature
            }
            
            # 发送请求到 /chat/completions 端点
            response = requests.post(
                f"{api_url.rstrip('/')}/chat/completions",
                headers=headers,
                json=payload,
                timeout=timeout
            )
            response.raise_for_status()
            result = response.json()
            
            # 解析OpenAI风格的响应
            if "choices" in result and len(result["choices"]) > 0:
                message = result["choices"][0].get("message", {})
                description = message.get("content", "无返回结果")
            else:
                description = result.get("content", result.get("text", "无返回结果"))
            
            return (description,)
            
        except requests.exceptions.RequestException as e:
            error_msg = f"[网络错误] {str(e)}"
            if hasattr(e, 'response') and e.response is not None:
                try:
                    error_detail = e.response.json()
                    error_msg += f"\n详细信息: {error_detail}"
                except:
                    error_msg += f"\n状态码: {e.response.status_code}"
            return (error_msg,)
        except Exception as e:
            return (f"[错误] {str(e)}",)

# 注册节点
NODE_CLASS_MAPPINGS = {
    "VL_QwenDescribeImage": VL_QwenDescribeImage
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "VL_QwenDescribeImage": "📷 Qwen VL Describe Image (OpenAI API)"
}
