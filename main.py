import openai
import gradio

openai.api_key = ""

messages = [{"role": "system", "content": "You are a someone needs tips for new year"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply


demo = gradio.Interface(fn=CustomChatGPT,
                    inputs=gradio.Textbox(label="ME", placeholder="Say what do you want"),
                    outputs=[gradio.Textbox(label="CHAT-GPT")],
                    title="SEIF ALDEN")

gradio.themes.builder()
demo.launch()
