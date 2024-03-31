from openai import OpenAI
import time
import pdb
client = OpenAI()
  
# assistant = client.beta.assistants.create(
#   name="Math Tutor",
#   instructions="You are a Finance professor at London school of Economics. You have extensive industry experience in finance and economics. You need to help me summarize the article in the files provided. Additionally,  identify 5 finance/economics terms from the article to help me build my financial literacy. Format the terms at the end of the response in a dictionary data structure format where the key is the term and value is the definition. For example, {term: definition, term2: definition2}.  Make sure the definitions are understandable for a college freshmen studying economics and finance",
#   tools=[{"type": "retrieval"}],
#   model="gpt-4-turbo-preview",
# )
# print(assistant)


# print(assistant_file)

def retrieve_assistant(assistant_id): 
  assistant_id = "asst_akYCcgxrI0FRYWdgzBdERB8m"
  assistant = client.beta.assistants.retrieve(assistant_id)
  return assistant

def create_thread():
  '''
  Threads represent conversations between a user and a assistant

  returns: thread object
  '''
  thread = client.beta.threads.create()
  return thread

def create_message(thread):
  '''
  Message objects are added to the thead 
  '''

  message = client.beta.threads.messages.create(
      thread_id=thread.id,
      role="user",
      content="Help me summarize the article in the files provided. Additionally, identify 5 finance/economics terms and definitions from the article in a dictionary data structure format"
  )

def run_thread(assistant, thread):
  '''
  Running a thread uses the model and tools associated with the Assistant to generate a response
  '''
  run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
    # instructions="Help me summarize the article in the files provided. Additionally, identify 5 finance/economics terms and definitions from the article in a dictionary data structure format"
  )
  # print("thread-id", thread.id)
  # print("run-id", run.id)
  
  while run.status in ['queued', 'in_progress', 'cancelling']:
    time.sleep(1) # Wait for 1 second
    run = client.beta.threads.runs.retrieve(
      thread_id=thread.id,
      run_id=run.id
    )
  if run.status == 'completed': 
    messages = client.beta.threads.messages.list(
      thread_id=thread.id
    )
    print(messages.data[0].content[0].text.value)
      
  else:
    print(run.status)

if __name__ == "__main__":
  assistant = retrieve_assistant("asst_akYCcgxrI0FRYWdgzBdERB8m")
  # print(assistant.instructions)
  # print(assistant)
  # assistant_file = client.beta.assistants.files.create(
  # assistant_id=assistant.id,
  # file_id="finance-article.txt"
  # )
  
  thread = create_thread()
  # print(thread.id)
  # message = create_message(thread)
  # print(message)
  run_thread(assistant, thread)
 