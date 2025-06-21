# Chatbot with RAG (Retrieval Augmented Generation)

A Python-based chatbot application that demonstrates how to build a chat app using large language models with retrieval augmented generation (RAG). This project shows how custom data, like PDFs, can be loaded and used for more meaningful and insightful chat responses.

## Features

- **Phase 1**: Basic chatbot setup and configuration
- **Phase 2**: Document loading and processing capabilities
- **Phase 3**: Advanced RAG implementation with vector storage

## Project Structure

```
├── README.md          # Project documentation
├── Pipfile            # Python dependencies (Pipenv)
├── Pipfile.lock       # Locked dependencies
├── phase_1.py         # Basic chatbot implementation
├── phase_2.py         # Document processing phase
└── phase_3.py         # Advanced RAG implementation
```

## Prerequisites

- Python 3.8+
- Pipenv (for dependency management)

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd Chatbot-with-RAG-main
```

2. Install dependencies using Pipenv:
```bash
pipenv install
```

3. Activate the virtual environment:
```bash
pipenv shell
```

## Usage

Each phase can be run independently:

```bash
# Run Phase 1 - Basic chatbot
python phase_1.py

# Run Phase 2 - Document processing
python phase_2.py

# Run Phase 3 - Advanced RAG
python phase_3.py
```

## How RAG Works

Retrieval Augmented Generation (RAG) enhances large language models by:

1. **Retrieval**: Finding relevant information from a knowledge base
2. **Augmentation**: Combining retrieved information with the user's query
3. **Generation**: Producing more accurate and contextual responses

This approach allows the chatbot to provide more informed answers based on specific documents or data sources.

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the [MIT License](LICENSE).
