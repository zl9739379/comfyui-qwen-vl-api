# ComfyUI Qwen VL & LLM API Node

🤖 A powerful ComfyUI custom node that integrates vision-language models and large language models through OpenAI-compatible APIs. Support both image analysis and text conversation modes.

![Node Preview](https://img.shields.io/badge/ComfyUI-Custom%20Node-orange) ![Python](https://img.shields.io/badge/Python-3.8+-blue) ![License](https://img.shields.io/badge/License-MIT-green)

## ✨ Features

- 🎯 **Dual Mode Operation**: Switch between vision analysis and text conversation
- 🖼️ **Image Analysis**: Describe, analyze, and understand images using vision-language models
- 💬 **Text Conversation**: Pure text chat with large language models
- 🔌 **API Flexibility**: Compatible with OpenAI-style APIs (SiliconFlow, OpenAI, etc.)
- ⚙️ **Rich Parameters**: Customizable temperature, max tokens, image quality, and more
- 🚀 **Easy Integration**: Simple drag-and-drop installation for ComfyUI

## 🚀 Quick Start

### Installation

1. **Clone or Download**
   ```bash
   cd ComfyUI/custom_nodes/
   git clone https://github.com/yourusername/comfyui-qwen-api-node.git
   ```

2. **Install Dependencies**
   ```bash
   pip install requests pillow numpy torch
   ```

3. **Restart ComfyUI**
   
   The node will appear in the node menu under `VL Model` category.

### Basic Usage

#### Vision Mode (Image Analysis)
1. Add the "🤖 Qwen VL & LLM API (Vision + Text)" node to your workflow
2. Connect an image input to the `image` port
3. Set `mode` to "vision"
4. Configure your API settings
5. Run the workflow

#### Text Mode (Pure Conversation)
1. Add the node to your workflow
2. Set `mode` to "text"
3. No need to connect image input
4. Enter your text prompt
5. Run the workflow

## 📋 Parameters

### Required Parameters
- **None** - All parameters are optional with sensible defaults

### Optional Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `image` | IMAGE | - | Input image (required for vision mode) |
| `api_url` | STRING | `https://api.siliconflow.cn/v1` | API server URL |
| `model` | STRING | `Qwen/Qwen2.5-VL-72B-Instruct` | Vision-language model name |
| `prompt` | STRING | `请描述这张图片的内容。` | Prompt for the model |
| `api_key` | STRING | `""` | API key for authentication |
| `timeout` | INT | `60` | Request timeout in seconds (10-300) |
| `max_tokens` | INT | `1000` | Maximum response tokens (100-4000) |
| `temperature` | FLOAT | `0.7` | Text generation randomness (0.0-2.0) |
| `image_quality` | INT | `95` | JPEG quality for image upload (50-100) |
| `detail` | CHOICE | `auto` | Image processing detail level |
| `mode` | CHOICE | `vision` | Operation mode: vision/text |
| `text_model` | STRING | `Qwen/Qwen2.5-72B-Instruct` | Model for text mode |

### Parameter Details

#### Mode Selection
- **vision**: Analyze images with vision-language models
- **text**: Pure text conversation with language models

#### Detail Levels
- **auto**: Automatically choose appropriate detail level
- **low**: Low resolution, faster processing
- **high**: High resolution, detailed analysis

## 🔧 API Configuration

### Supported APIs

#### SiliconFlow (Default)
```
API URL: https://api.siliconflow.cn/v1
Models: Qwen/Qwen2.5-VL-72B-Instruct, Qwen/Qwen2.5-72B-Instruct
```

#### OpenAI
```
API URL: https://api.openai.com/v1
Models: gpt-4-vision-preview, gpt-4, gpt-3.5-turbo
```

#### Other Compatible APIs
Any OpenAI-compatible API service can be used by adjusting the `api_url` and `model` parameters.

### Getting API Keys

1. **SiliconFlow**: Visit [SiliconFlow](https://siliconflow.cn) to get your API key
2. **OpenAI**: Visit [OpenAI Platform](https://platform.openai.com) to get your API key

## 💡 Usage Examples

### Example 1: Image Description
```
Input: [Image of a cat]
Prompt: "Describe this image in detail, including colors, objects, and scene."
Mode: vision
Output: "This image shows a fluffy orange tabby cat sitting on a wooden table..."
```

### Example 2: Technical Image Analysis
```
Input: [Diagram or chart]
Prompt: "Analyze this technical diagram and explain its components."
Mode: vision
Output: "This diagram illustrates a network architecture with..."
```

### Example 3: Text Conversation
```
Input: No image needed
Prompt: "Explain the concept of machine learning in simple terms."
Mode: text
Output: "Machine learning is a subset of artificial intelligence..."
```

### Example 4: Creative Writing
```
Input: No image needed
Prompt: "Write a short story about a robot learning to paint."
Mode: text
Output: "In a small workshop filled with canvases and brushes..."
```

## 🛠️ Advanced Configuration

### Custom Model Configuration
```python
# For vision tasks
model = "your-custom-vision-model"
mode = "vision"

# For text tasks  
text_model = "your-custom-text-model"
mode = "text"
```

### Performance Optimization
- **Low Detail Mode**: Use `detail="low"` for faster processing
- **Reduced Tokens**: Lower `max_tokens` for quicker responses
- **Image Quality**: Adjust `image_quality` based on needs vs. speed

### Error Handling
The node provides detailed error messages for:
- Network connectivity issues
- API authentication problems
- Invalid model configurations
- Missing image inputs (in vision mode)

## 🔍 Troubleshooting

### Common Issues

#### "Network Error" Messages
- Check your internet connection
- Verify API URL is correct
- Ensure API key is valid and has sufficient credits

#### "Missing Image" Error
- Make sure image is connected when using vision mode
- Switch to text mode if you don't need image analysis

#### Slow Response Times
- Reduce `max_tokens` for faster responses
- Use `detail="low"` for quicker image processing
- Consider using smaller models

#### API Key Issues
- Ensure API key is correctly formatted
- Check if API key has necessary permissions
- Verify account has sufficient credits/quota

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) - The amazing UI for Stable Diffusion
- [Qwen Team](https://github.com/QwenLM/Qwen) - For the excellent vision-language models
- [SiliconFlow](https://siliconflow.cn) - For providing accessible API services


Powered by claude.ai

⭐ If this project helps you, please consider giving it a star on GitHub!
