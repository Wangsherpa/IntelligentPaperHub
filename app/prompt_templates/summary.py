BASIC_SUMMARIZER_TEMPLATE = """Please provide a concise and accurate summary of the most important points from the text below.  
Focus on key concepts, events, and any critical details. If there are specific sections that deserve more emphasis or clarity, include them in your summary.

Here is the text to summarize:
{text_document}
"""

REFINE_SUMMARIZER_TEMPLATE = """
Here is a partial summary that has already been generated: 
{previous_summary}
Please refine and improve this summary. Focus on the following:
- Correct any inaccuracies or missing key details.
- If some sections are unclear, elaborate on them.
- Make the language more concise and readable, while preserving essential information.
- Add any important context or details that might have been missed, ensuring completeness."**

Here is the original text again for reference: 
{text_document}
"""
