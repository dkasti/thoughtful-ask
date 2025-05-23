"""Load Q&A pairs from a JSON file."""

import logging

from agent import SupportAgent

# Configure logging to file and stdout
logger = logging.getLogger()
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("support_agent.log")
file_handler.setFormatter(
    logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
)
logger.addHandler(file_handler)

console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter("%(message)s"))
logger.addHandler(console_handler)


def run_cli():
    """
    Run the command-line interface for the support agent."""
    qna_file = "data/qna.json"
    agent = SupportAgent(qna_file)
    print("Welcome to Thoughtful AI Support Agent! (type 'exit' to quit)")

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() in ("exit", "quit"):
            print("Support Agent: Goodbye! Have a great day.")
            break

        answer = agent.get_answer(user_input)
        print(f"Support Agent: {answer}\n")
        logger.info("Q: %s | A: %s", user_input, answer)


if __name__ == "__main__":
    run_cli()
