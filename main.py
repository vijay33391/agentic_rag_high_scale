import logfire
from dotenv import load_dotenv
load_dotenv()
logfire.configure()
def main():
    print("Hello from production-agentic-rag-kubernetes!")

# validate the logfire
def validate_logfire():
    print("Validating logfire...")
    logfire.info("Logfire is working!")

if __name__ == "__main__":
    main()
    validate_logfire()
