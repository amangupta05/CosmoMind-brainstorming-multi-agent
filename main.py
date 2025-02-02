from orchestrator import run_brainstorm

def main():
    # Run the brainstorming orchestrator.
    final_response = run_brainstorm()
    
    # Print the final response for inspection.
    print("=== Final Response ===")
    print(final_response)

if __name__ == "__main__":
    main()
