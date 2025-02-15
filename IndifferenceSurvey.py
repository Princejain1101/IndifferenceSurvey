import streamlit as st
import pandas as pd

# st.image('https://drive.google.com/file/d/1xxYDKH__7eFlGW5JGkTqgOd30_jtCs1f/view?usp=sharing', use_container_width=True)
# # st.markdown("![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)")
st.image([img for img in ["airforce1.png","airforce1ambush.png"]], width=350)
price = 150
if "same_price_question" not in st.session_state:
    st.session_state["same_price_question"] = None
if "not_buy_ambush_question" not in st.session_state:
    st.session_state["not_buy_ambush_question"] = None
if "verify_not_buy_ambush_question" not in st.session_state:
    st.session_state["verify_not_buy_ambush_question"] = None
if "indifference_question" not in st.session_state:
    st.session_state["indifference_question"] = None
if "verify_indifference_question_partA" not in st.session_state:
    st.session_state["verify_indifference_question_partA"] = None
if "verify_indifference_question_partB" not in st.session_state:
    st.session_state["verify_indifference_question_partB"] = None

with st.form(key='buy ambush form at same price'):
    st.write("Consider this case scenario... ")
    st.write("Price of Option1 AirForce1 is \$" + str(price) + " and Price of Option2 AirForce1Ambush is \$" + str(price))
    same_price = st.radio("Q1. Which sneaker do you prefer?", ("Option1 AirForce1", "Option2 AirForce1Ambush", "indifferent"))
    if st.form_submit_button("Confirm Sneaker at Same Price"):
        if same_price == "Option1 AirForce1":
            st.write("Option1 AirForce1 is chosen, so you are likely not a right candidate. Please exit the survey.")
            if st.form_submit_button("Exit the survey"):
                st.stop()
        elif same_price == "Option2 AirForce1Ambush":
            st.write("Option2 AirForce1Ambush is chosen")
            st.session_state["same_price_question"] = same_price
        else:
            st.write("You are indifferent which is probably not right. Please exit the survey")
            if st.form_submit_button("Exit the survey"):
                st.stop()
if st.session_state["same_price_question"] is not None:
    with st.form(" Not Buy AirForce1Ambush Price"):
        not_buy_ambush_price = st.number_input("Q2. What price would the Ambush need to be for you to choose the AF1 instead?", min_value=0, max_value=10000, step=1)
        if st.form_submit_button("Confirm Not buy Ambush Price"):
            st.session_state["not_buy_ambush_question"] = not_buy_ambush_price
if st.session_state["not_buy_ambush_question"] is not None:
    with st.form(" Verify Not Buy Ambush Price"):
        verify_not_buy_ambush = st.radio("Q3. Would you buy Option1 AirForce1 at \$"+str(price)+" if Option2 AirForce1Ambush is at \$"+str(st.session_state["not_buy_ambush_question"])+" price?", ("Yes", "No"))
        if st.form_submit_button("Confirm Verify Not buy Ambush Price"):
            if verify_not_buy_ambush == "Yes":
                # st.write("Move Forward")
                st.session_state["verify_not_buy_ambush_question"] = verify_not_buy_ambush
            else:
                # st.write("Go back to question2")
                st.session_state["not_buy_ambush_question"] = None
                st.warning("You have not chosen a correct price for Option2 Airforce1Ambush then. Please try again.")
                if st.form_submit_button("Try Again"):
                    st.rerun()
if st.session_state["verify_not_buy_ambush_question"] is not None:
    st.write("Based on the previous exercises you picked the Option2 AirForce1 Ambush when the price were \$" + str(
        price) + " each whereas you picked the Option1 AirForce1 when price for the Option2 AirForce1Ambush  were \$" + str(
        st.session_state["not_buy_ambush_question"]) + " and the price of the Option1 AirForce1 was \$" + str(price))
    st.write("Hence there is a value between \$" + str(price) + " and \$" + str(st.session_state[
                                                                                    "not_buy_ambush_question"]) + " at which you are indifferent between the two sneakers (i.e. you cannot choose between them)")
    with st.form(" Indifference question"):
        indifference_number = st.number_input("Q4. Please fill out the price for the Option2 AirForce1Ambush at which you are indifferent between the 2 sneakers.", min_value=price, max_value=st.session_state["not_buy_ambush_question"], step=1)
        if st.form_submit_button("Confirm Indifference question"):
            st.session_state["indifference_question"] = indifference_number
if st.session_state["indifference_question"] is not None:
    with st.form(" Verify Indifference question partA"):
        st.write("Price for Option1 Airforce1 at\$"+str(price)+" and Option2 Airforce1Ambush at \$"+str(st.session_state["indifference_question"]))
        verify_indifferenceA = st.radio("Q5A. Can the program select option 2 AirForce1Ambush for you? Are you OK with that?", ("Yes", "No"))
        if st.form_submit_button("Confirm Verify Indifference question partA"):
            if verify_indifferenceA == "Yes":
                # st.write("Move Forward")
                st.session_state["verify_indifference_question_partA"] = verify_indifferenceA
            else:
                st.warning("You are not truly indifferent since you prefer option 1. ")
                st.warning("Hence the price of \$"+str(st.session_state["indifference_question"]) +" is too high for you to be indifferent. Please select a price for option 2 at which you are truly indififerent.")
                st.session_state["indifference_question"] = None
                if st.form_submit_button("Please select the indifference price again."):
                    st.rerun()
if st.session_state["verify_indifference_question_partA"] is not None:
    with st.form(" Verify Indifference question partB"):
        st.write("Price for Option1 Airforce1 at\$"+str(price)+" and Option2 Airforce1Ambush at \$"+str(st.session_state["indifference_question"]))
        verify_indifferenceB = st.radio("Q5B. Can the program select option 1 AirForce1 for you? Are you OK with that?", ("Yes", "No"))
        if st.form_submit_button("Confirm Verify Indifference question partB"):
            if verify_indifferenceB == "Yes":
                # st.write("Move Forward")
                st.session_state["verify_indifference_question_partB"] = verify_indifferenceB
            else:
                st.warning("You are not truly indifferent since you prefer option 2. ")
                st.warning("Hence the price of \$"+str(st.session_state["indifference_question"]) +" is too low for you to be indifferent. Please select a price for option 2 at which you are truly indififerent.")
                st.session_state["indifference_question"] = None
                st.session_state["verify_indifference_question_partA"] = None
                if st.form_submit_button("Please select the indifference price again."):
                    st.rerun()
if st.session_state["verify_indifference_question_partB"] is not None:
    st.write("Thank you for taking the Indifference survey!")
    st.stop()
