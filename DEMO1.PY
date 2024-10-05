from dotenv import load_dotenv  
from langchain_core.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
import os

if __name__=="__main__":
    load_dotenv()
    print("Hello World")
    print(os.environ['OPEN_API_KEY'])

information="""
Mahendra Singh Dhoni (/məˈheɪndrə ˈsɪŋ dhæˈnɪ/ ⓘ; born 7 July 1981) is an Indian professional cricketer who plays as a 
right-handed batter and a wicket-keeper. Widely regarded as one of the most prolific wicket-keeper batsmen and captains,
 he represented the Indian cricket team and was the captain of the side in limited overs formats from 2007 to 2017 and in 
 test cricket from 2008 to 2014. Dhoni has captained the most international matches and is the most successful Indian captain. 
 He has led India to victory in the 2007 ICC World Twenty20, the 2011 Cricket World Cup, and the 2013 ICC Champions Trophy, 
 being the only captain to win three different limited overs ICC tournaments. He also led the teams that won the Asia Cup in 2010, 
 2016 and was a member of the title winning squad in 2018.

"""

summary_prompt = """ Based on the given input {information}. Can you generate the 
                                                       a. Summary
                                                       b. 2 Key Highlight points"""


summary_prompt_template = PromptTemplate(input_variables=["information"],template=summary_prompt)

llm = ChatOpenAI(temperature=0.4,model_name="gpt-3.5-turbo")
chain=summary_prompt_template|llm
res =chain.invoke(input={'information':information})

print(res)


