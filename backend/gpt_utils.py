from openai import OpenAI
import time
from dotenv import load_dotenv
import os
import pdb
import json

load_dotenv()

def retrieve_assistant(): 
  assistant_id = os.getenv("OAI_ASS_KEY")
  assistant = client.beta.assistants.retrieve(assistant_id)
  return assistant

def create_thread():
  '''
  Threads represent conversations between a user and a assistant

  returns: thread object
  '''
  thread = client.beta.threads.create()
  return thread

def create_message(thread_id):
  '''
  Message objects are added to the thread 
  '''
  file = client.files.create(
    file=open("test_article.txt", "rb"),
    purpose="assistants")
  
  thread_message = client.beta.threads.messages.create(
    thread_id=thread_id,
    role="user",
    content="Help me summarize the article in the attachment. Additionally, identify 5 financial terms in the article that can help improve my financial literacy. Your response MUST be in JSON string format with the summary and list of definitions",
    attachments=[{"file_id": file.id, "tools": [{"type": "file_search"}]}]
  )

  return file.id
                                                        

def run_thread(assistant, thread, file_id):
  '''
  Running a thread uses the model and tools associated with the Assistant to generate a response
  '''
  run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id
  )
  
  while run.status in ['queued', 'in_progress', 'cancelling']:
    time.sleep(1)
    run = client.beta.threads.runs.retrieve(
      thread_id=thread.id,
      run_id=run.id
    )
  if run.status == 'completed': 
    messages = client.beta.threads.messages.list(
      thread_id=thread.id
    )
    # return messages.data[0].content[0].text.value
    return(json.loads(messages.data[0].content[0].text.value))
    client.files.delete(file_id)
    return data
      
  else:
    print(run.status)

def initialize_gpt():
  global client
  client = OpenAI(api_key=os.getenv("OAI_API_KEY"))
  assistant = retrieve_assistant()
  thread = create_thread()
  return assistant, thread


# if __name__ == "__main__":
  # client = OpenAI(api_key=os.getenv("OAI_API_KEY"))
  # assistant = retrieve_assistant()
  # print(assistant)
  # with open('test_article.txt', 'rb') as fp:
  #   content = fp.read()

  # thread = create_thread()
  # messsage = create_message(thread.id)
  # data = run_thread(assistant, thread)

 