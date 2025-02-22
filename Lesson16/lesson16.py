import streamlit as st

from Lesson4.whileloops import user_input


def main():
    st.title("Hello World")

if __name__ == '__main__':
    main()

if st.button("Click ME !"):
    st.write("CLICKED!")

    st.checkbox("Check Me")

if st.checkbox("Check for some text"):
    st.write("YOU CLICKED BECASUE YOU ARE SUTPID")


user_input = st_input("Enter text" , "Shkruaj nje text")
st.write("You entered: " ,user_input)


age = st.number_input("Enter your age " , min_value = 1 , max_value = 100)
st.write(f"Your age: {age}")

message = st.textarea("Enter a message")
st.write(f"Your message , {message}")


choice = st.radio("Choose one: " ['Choice 1 , Choice 2 , Choice 3'])
st.write(f"You chose , {choice}")



if st.button("Sucess"):
    st.success()

try:
    1/0
except Exception as e:
    st.write(e)