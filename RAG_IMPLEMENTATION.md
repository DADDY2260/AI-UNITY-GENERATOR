# RAG (Retrieval-Augmented Generation) Implementation

## Overview

This project now includes a **RAG (Retrieval-Augmented Generation)** pipeline that enhances the AI Unity Game Generator by providing access to a specialized knowledge base of game design principles and Unity-specific information.

## What is RAG?

**RAG** combines **retrieval** of relevant information from a knowledge base with **generation** of responses using a language model. Instead of relying solely on the model's training data, RAG:

1. **Retrieves** relevant documents/information from a knowledge base
2. **Augments** the LLM's context with this retrieved information  
3. **Generates** more accurate, up-to-date, and contextually relevant responses

## Benefits for Your Unity Game Generator

### Before RAG
- Generic suggestions based on general training data
- Limited Unity-specific guidance
- No access to current best practices
- Potential for outdated information

### After RAG
- **Specific Unity guidance**: Retrieves Unity-specific implementation details
- **Game design expertise**: Access to proven game design principles
- **Current best practices**: Updatable knowledge base
- **Reduced hallucinations**: Grounded in factual information
- **Domain expertise**: Specialized knowledge for different game genres

## Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Game Idea     │───▶│   RAG Pipeline   │───▶│  Enhanced LLM   │
│   Description   │    │                  │    │   Response      │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                              │
                              ▼
                       ┌──────────────────┐
                       │  Knowledge Base  │
                       │                  │
                       │ • Game Design    │
                       │ • Unity Specific │
                       │ • Best Practices │
                       └──────────────────┘
```

## Knowledge Base Structure

The RAG system maintains a structured knowledge base with the following categories:

### 1. Game Design (`game_design`)
- **platformer_mechanics**: Double jump, wall jumping, dash abilities
- **rpg_elements**: Character progression, inventory systems, quest systems
- **shooter_mechanics**: Aim mechanics, weapon systems, cover systems
- **puzzle_elements**: Logic puzzles, physics-based challenges

### 2. Unity Specific (`unity_specific`)
- **player_controller**: Input handling, movement, physics
- **game_management**: Game state, scene management, data persistence
- **ui_systems**: Canvas, UI components, event handling
- **audio_systems**: Audio sources, mixing, 3D audio

### 3. Best Practices (`best_practices`)
- **code_organization**: Script structure, inheritance, interfaces
- **performance**: Object pooling, optimization, memory management
- **user_experience**: Feedback, accessibility, intuitive design

## Implementation Details

### Core Components

#### 1. RAGPipeline Class (`backend/app/rag/rag_pipeline.py`)
```python
class RAGPipeline:
    def __init__(self, knowledge_base_path: str = "knowledge_base")
    def retrieve_relevant_info(self, query: str, top_k: int = 5)
    def enhance_prompt_with_rag(self, original_prompt: str, game_idea: str, genre: str)
    def add_to_knowledge_base(self, category: str, subcategory: str, content: List[str])
```

#### 2. Enhanced GameEnhancer (`backend/app/llm/game_enhancer.py`)
- Now integrates RAG pipeline
- Enhances prompts with retrieved knowledge
- Provides more specific, actionable suggestions

#### 3. API Endpoints (`backend/app/main.py`)
- `GET /rag/stats`: Get knowledge base statistics
- `POST /rag/add-knowledge`: Add new knowledge
- `GET /rag/search`: Search knowledge base

### Search Algorithm

The RAG system uses **TF-IDF (Term Frequency-Inverse Document Frequency)** with **cosine similarity** for retrieval:

1. **Vectorization**: Convert documents and queries to TF-IDF vectors
2. **Similarity Calculation**: Compute cosine similarity between query and documents
3. **Ranking**: Return top-k most similar documents
4. **Threshold Filtering**: Only return results above similarity threshold

## Usage Examples

### 1. Enhanced Game Idea Generation

**Before RAG:**
```
Input: "2D platformer where a fox collects gems"
Output: Generic suggestions like "add jumping mechanics"
```

**After RAG:**
```
Input: "2D platformer where a fox collects gems"
Output: Specific suggestions like:
- "Implement double jump using Input.GetAxis and Rigidbody2D forces"
- "Add collectible system with ScriptableObject-based items"
- "Use Animator for smooth fox movement animations"
```

### 2. Adding New Knowledge

```python
# Add new game design knowledge
rag_pipeline.add_to_knowledge_base(
    category="game_design",
    subcategory="procedural_elements",
    content=[
        "Procedural generation creates infinite replayability",
        "Roguelike elements add challenge and variety"
    ]
)
```

### 3. Searching Knowledge Base

```python
# Search for relevant information
results = rag_pipeline.retrieve_relevant_info("Unity player movement", top_k=3)
for result in results:
    print(f"- {result['content']} (Score: {result['similarity_score']:.3f})")
```

## API Endpoints

### Get Knowledge Base Statistics
```bash
curl http://localhost:8000/rag/stats
```

Response:
```json
{
  "status": "success",
  "stats": {
    "total_items": 45,
    "categories": {
      "game_design": 20,
      "unity_specific": 15,
      "best_practices": 10
    },
    "document_count": 45
  }
}
```

### Add New Knowledge
```bash
curl -X POST http://localhost:8000/rag/add-knowledge \
  -H "Content-Type: application/json" \
  -d '{
    "category": "game_design",
    "subcategory": "new_mechanics",
    "content": [
      "Time manipulation mechanics add unique gameplay",
      "Environmental storytelling through level design"
    ]
  }'
```

### Search Knowledge Base
```bash
curl "http://localhost:8000/rag/search?query=Unity%20player%20movement&top_k=3"
```

## Testing

Run the RAG test suite:

```bash
python test_rag.py
```

This will test:
- ✅ RAG pipeline initialization
- ✅ Knowledge base search functionality
- ✅ Prompt enhancement
- ✅ Knowledge addition
- ✅ Game enhancer integration

## Future Enhancements

### 1. Advanced Embeddings
- Replace TF-IDF with more sophisticated embeddings (e.g., OpenAI embeddings)
- Support for semantic similarity beyond keyword matching

### 2. Dynamic Knowledge Base
- Automatic knowledge extraction from Unity documentation
- Integration with game design blogs and tutorials
- Community-contributed knowledge

### 3. Multi-Modal RAG
- Include Unity code examples in knowledge base
- Support for image-based game design references
- Video tutorials and demonstrations

### 4. Personalized Knowledge
- User-specific knowledge bases
- Learning from generated projects
- Feedback loop for continuous improvement

## Installation and Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Environment Variables
```bash
export OPENAI_API_KEY="your_openai_api_key"
```

### 3. Initialize Knowledge Base
The RAG system will automatically create a default knowledge base on first run.

### 4. Test the Implementation
```bash
python test_rag.py
```

## Performance Considerations

### Memory Usage
- Knowledge base is loaded into memory for fast retrieval
- TF-IDF vectors are pre-computed
- Consider chunking for very large knowledge bases

### Search Performance
- TF-IDF similarity is computationally efficient
- Results are cached for repeated queries
- Top-k retrieval limits result set size

### Scalability
- Knowledge base can be distributed across multiple files
- Support for incremental updates
- Easy to extend with new categories and subcategories

## Troubleshooting

### Common Issues

1. **Import Errors**: Ensure all dependencies are installed
   ```bash
   pip install scikit-learn numpy
   ```

2. **OpenAI API Errors**: Check your API key
   ```bash
   echo $OPENAI_API_KEY
   ```

3. **Knowledge Base Not Found**: The system will create a default one
   ```bash
   ls knowledge_base/
   ```

4. **Search Returns Empty Results**: Check your query terms
   ```bash
   curl "http://localhost:8000/rag/search?query=platformer"
   ```

## Contributing

### Adding New Knowledge
1. Identify the appropriate category and subcategory
2. Add specific, actionable content
3. Test with relevant queries
4. Update documentation if needed

### Improving Search
1. Experiment with different vectorization methods
2. Adjust similarity thresholds
3. Add more diverse training data
4. Implement feedback mechanisms

---

**🎉 Your Unity Game Generator now has enterprise-grade RAG capabilities!** 