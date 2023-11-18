# Import necessary libraries
from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager
import autogen

#load_dotenv(find_dotenv())
captured_messages=[]

# Autogen configuration
config_list = [{'model': 'gpt-4-1106-preview', 'api_key': 'sk-.'}]
llm_config = {"seed": 42, "config_list": config_list, "temperature": 0.6}

# Define Autogen agents
johnny = AssistantAgent(name="Johnny", llm_config=llm_config, system_message="As Johny Silverhand from cyberpunk 2077, you're trying to solve the Bob's problem. You are talking mostly with Micheal Scott. Your answers are short but valueble. Type in style you are using all day. If you agreed with others type TERMINATE")
michael = AssistantAgent(name="Michael", llm_config=llm_config, system_message="As Michael Scott from the office series, you're talking with Johnny and trying to solve Bob's problem. Type in style you are using all day. Your answers are short but valueble. If you agreed with others type TERMINATE")
user_proxy = UserProxyAgent(name="Karolina", llm_config=llm_config, system_message="You know Bob the best. In conversation you are answer ONLY if someone is not sure what Bob's like. You are not activily participating in conversation. If you think that guys found the perfect solution type TEMINATE", human_input_mode="NEVER")

def capture_messages(recipient, messages, sender, config):
    global captured_messages  # Reference the global variable
    captured_message = messages[-1]  # Assuming messages is a list of JSON messages
    captured_messages.append(captured_message)  # Append the message to the global list
    print(f"Message from: {sender.name} to: {recipient.name} | Message: {captured_message}")
    return False, None


# Register capture_messages function with each bot
johnny.register_reply(
    [autogen.Agent, None],
    reply_func=capture_messages,
    config={"callback": None},
)

michael.register_reply(
    [autogen.Agent, None],
    reply_func=capture_messages,
    config={"callback": None},
)

user_proxy.register_reply(
    [autogen.Agent, None],
    reply_func=capture_messages,
    config={"callback": None},
)


# Group chat setup
groupchat = GroupChat(agents=[user_proxy, johnny, michael], messages=[], max_round=4)
manager = GroupChatManager(groupchat=groupchat, llm_config=llm_config)


def text_to_list(messages):
    dialogues = []
    for msg in messages:
        if 'content' in msg and 'name' in msg:
            character = msg['name']
            dialogue = msg['content']
            dialogues.append((character, dialogue))
        else:
            print(f"Skipping invalid message: {msg}")
    print("Extracted dialogues:", dialogues)
    return dialogues


# Example usage
task = "Guys. Karolina here, Bob assistant, greatest friend. Bob wants to find new hobby. He already dancing bachata and going to gym. What's your advice?"
user_proxy.initiate_chat(manager, message=task)