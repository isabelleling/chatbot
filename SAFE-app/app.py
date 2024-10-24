import streamlit as st
import random

def init_session():
    """Presents a food waste sorting quiz with one item and three options."""

    questions = [
        {
            "q": "Coffee grounds",
            "a": "compost",
            "i": "coffee_grounds.jpg",
        },
        {
            "q": "Plastic food container",
            "a": "recycle",
            "i": "plastic_food_container.jpg",
        },
        {
            "q": "Banana peel",
            "a": "compost",
            "i": "banana_peel.webp",
        },
        {
            "q": "Egg shells",
            "a": "compost",
            "i": "egg_shells.jpeg",
        }
    ]

    explanations = {
        "compost": "Compostable materials break down into nutrient-rich soil.",
        "recycle": "Recyclable materials can be processed to create new products.",
        "trash": "Trash is disposed of in landfills and doesn't decompose easily.",
    }

    # Initialize session state variables
    if "questions" not in st.session_state:
        st.session_state.total_questions = len(questions)
        st.session_state.questions = questions
        random.shuffle(st.session_state.questions)
        st.session_state.explanations = explanations
        st.session_state.answered = False
        st.session_state.correct_answers = 0  # Track correct answers
        st.session_state.current_question = 0  # Track current question

def closing_statement(right, total):
    # Calculate the percentage of correct answers
    st.image("congrats.jpg")
    correct_percentage = (right / total) * 100
    screen_time = 53 * right
    st.subheader("Thank you for playing :blue[Sort Appropriately For Earth (SAFE)!]", divider=True)
    st.subheader(
        f"You answered **{right}** out of **{total}** questions correctly.")
    st.subheader(f"Your score: **{correct_percentage:.1f}%**")
    if right == 0:
        st.subheader(f"You could try :red[**a little bit harder**] to save the Earth! :sunglasses:")
    else:
        st.subheader(f"You deserve :red[**{screen_time}**] minutes of screen time for saving the Earth!")


def draw_bins(item):
    bin_images = [
        {
            "src": "trash.png",
            "value": "trash",
        },
        {
            "src": "recycle.png",
            "value": "recycle",
        },
        {
            "src": "compost.png",
            "value": "compost",
        },
    ]

    cols = st.columns(3)
    choice = None
    for i, bin in enumerate(bin_images):
        with cols[i]:
            s = bin["src"]
            v = bin["value"]
            if st.button(f"Sort :red[**{item}**] in the :blue[**{v}**] bin...", 
                         key=v):
                choice = v
            st.image(s)

    return choice

def food_waste_quiz():
    init_session()

    # Check if all questions have been answered
    if st.session_state.current_question >= st.session_state.total_questions:
        closing_statement(st.session_state.correct_answers, 
                          st.session_state.total_questions)
        return  # End the function to prevent further execution

    # st.write(f"000 Where does **{st.session_state}**belong?")
    st.subheader(f":blue[Sort Appropriately For Earth (SAFE)!]", divider=True)

    # Display the quiz question
    x = st.session_state.questions[st.session_state.current_question]
    q = x["q"]
    a = x["a"]
    i = x["i"]
    e = st.session_state.explanations[a]
    st.write(f"Which bin should you sort :red[**{q}**]?")
    st.image(i, use_column_width=True)

    # draw 3 bins
    user_choice = draw_bins(q)

    # Validate the user's choice
    # st.write(f"2 - Where does **{q}** **{st.session_state}**belong?")
    if user_choice:
        # st.write(f"3 - Where does **{q}** **{st.session_state}**belong?")
        if user_choice == a:
            if not st.session_state.answered:
                st.session_state.answered = True
                # collect right answer only once
                st.session_state.correct_answers += 1
            st.write("✅ **That's correct!** 🎉")
            st.write(f":blue[You got it -- {e}]")
        else:
            # st.write(f"❌ **Incorrect.** {q} goes in the **{a}** bin.")
            st.write(f"❌ **Incorrect.")
            st.write(f":red[Try again or skip to next question.]")

    # Display a "Next Question" button
    if st.button("Next Question"):
        st.session_state.answered = False
        st.session_state.current_question += 1
        st.rerun()  # Refresh the page for the next question


# Run the quiz function
if __name__ == "__main__":
    food_waste_quiz()
