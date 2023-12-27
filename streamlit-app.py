
import streamlit as st
import pickle   
import numpy as np

with open("blstm_model.pkl","rb") as file:
  data = pickle.load(file)
model_blstm = data["model"]





# print(model_blstm.predict(
#   [""" /CWE_Trapdoor__ip_based_logic_.c send \nvoid CWE_Trapdoor__ip_based_logic__bad() \nWSADATA wsaData ; \nstruct sockaddr_in service , acceptService ; \nif ( WSAStartup ( MAKEWORD (  ,  ) , & wsaData ) != NO_ERROR )  \nlistenSocket = socket ( AF_INET , SOCK_STREAM , IPPROTO_TCP ); \nif ( listenSocket == INVALID_SOCKET )  \nmemset ( & service ,  , sizeof ( service ) ); \nservice . sin_family = AF_INET; \nservice . sin_addr . s_addr = INADDR_ANY; \nservice . sin_port = htons (  ); \nif ( bind ( listenSocket , ( struct sockaddr * ) & service , sizeof ( service ) ) == SOCKET_ERROR )  \nif ( listen ( listenSocket ,  ) == SOCKET_ERROR )  \nacceptSocket = accept ( listenSocket , NULL , NULL ); \nif ( acceptSocket == SOCKET_ERROR )  \nif ( getsockname ( acceptSocket , ( struct sockaddr * ) & acceptService , & acceptServiceLen ) == -  )  \nif ( strcmp ( "..." , inet_ntoa ( acceptService . sin_addr ) ) ==  )  \nif ( send ( acceptSocket , ADMIN_MESSAGE , strlen ( ADMIN_MESSAGE ) ,  ) == SOCKET_ERROR )  \nif ( send ( acceptSocket , DEFAULT_MESSAGE , strlen ( DEFAULT_MESSAGE ) ,  ) == SOCKET_ERROR )  \nwhile (  )  \n\n"""]

#   ))

CWE = ["non-vulnerable","CWE-404","CWE-476","CWE-119","CWE-706","CWE-670","CWE-673","CWE-119, CWE-666, CWE-573","CWE-573","CWE-668"," CWE-400, CWE-665, CWE-020"," CWE-662"," CWE-400"," CWE-665"," CWE-020",
       " CWE-074"," CWE-362"," CWE-191"," CWE-190"," CWE-610"," CWE-704"," CWE-170"," CWE-676"," CWE-187"," CWE-138"," CWE-369"," CWE-662, CWE-573"," CWE-834"," CWE-400, CWE-665"," CWE-400, CWE-404"," CWE-221",
       " CWE-754"," CWE-311"," CWE-404, CWE-668"," CWE-506"," CWE-758"," CWE-666"," CWE-467"," CWE-327"," CWE-666, CWE-573"," CWE-469"]




def source_code_c_to_tcode_gadget(code):
  lines = code.splitlines()
  code_gadget = ""
  for line_number, line in enumerate(lines, start=1):
      # if line_number == 11:
      #     print(line)
      line = line.strip().replace("""{""", """ """).replace("""}""", """""")
      if line == '\n' or line == "":
          continue
      code_gadget += line + '\n'
  return code_gadget




def show_predict_page():
  st.title("CWE classification")
  st.write("### we need information to predict")
  user_input_text = st.text_input("Enter something:")

    # Button to execute print("a")
  if st.button("OK"):
    user_input_array = np.array([user_input_text])
    result = model_blstm.predict(user_input_array)
    #st.write(f"Result: {result}")


    max_index = np.argmax(result)
    #st.write(f"Index of Max Value: {max_index}")

    st.write("CWE type:")
    st.write(f"{CWE[max_index]}")


show_predict_page()




# Run 
# ./venv/Scripts/activate   
# streamlit run streamlit-app.py