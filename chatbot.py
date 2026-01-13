faqs = {
    "what is codealpha": "CodeAlpha is an internship platform.",
    "how to apply": "You can apply through the CodeAlpha website.",
    "is it free": "Yes, this internship is completely free.",
    "what is task 2": "Task 2 is creating a chatbot for FAQs."
}

print("FAQ Chatbot (Type 'exit' to stop)")

while True:
    question = input("Ask your question: ").lower()

    if question == "exit":
        print("Thank you!")
        break

    found = False
    for q in faqs:
        if q in question:
            print("Answer:", faqs[q])
            found = True
            break

    if not found:
        print("Sorry, I don't understand your question.")
