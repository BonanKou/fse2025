# Prompt 1
prompt1 = '''
INSTRUCTION:
Create a comprehensive API document for {api_name}, based on the seven knowledge types described below. Ensure each section is concise, actionable, and specific to the API's functionality, while maintaining clarity and detail.

API DESCRIPTION:
{api_description}

KNOWLEDGE TYPE REQUIREMENTS:

Functionality: Describe the operations or actions this API can perform.
Concept: Explain fundamental ideas and terminologies to help users understand and utilize this API.
Pattern: Provide common use cases and examples of solving specific problems using this API.
Directive: Offer guidelines, best practices, and things to avoid when using this API.
Performance: Detail the time and memory efficiency characteristics of this API.
Environment: Specify the conditions, system requirements, or configurations required for this API to function properly.
Alternative: Suggest other APIs that offer similar functionality, including complementary or replacement options.
'''

# Prompt 2
prompt2 = '''
INSTRUCTION:
Generate a comprehensive and practical API document for {api_name} tailored to developers and integrators. Focus on providing actionable insights and structured sections that align with the seven knowledge types described below.

API DESCRIPTION:
{api_description}

KNOWLEDGE TYPE BREAKDOWN:

Functionality:

What can this API do?
Provide concise examples of the actions or outputs it facilitates.
Concepts:

What are the key terminologies, methods, or ideas relevant to this API?
Include definitions and their importance in context.
Patterns:

What are the most common use cases for this API?
Provide code snippets and practical scenarios.
Directives:

What are the dos and don’ts when using this API?
Highlight best practices for seamless integration.
Performance:

How does this API perform in terms of speed and resource usage?
Provide benchmarks or known limitations.
Environment:

What are the required configurations or dependencies?
Highlight supported platforms and system requirements.
Alternatives:

Are there APIs with similar functionality?
Provide comparisons and suggest complementary tools.
'''
