from app.ai.llm import call_llm


class RepairEngine:

    def fix_prompt(self, prompt: str, diagnosis: str):

        return call_llm([
            {
                "role": "system",
                "content": "Improve this prompt to fix generation failure."
            },
            {
                "role": "user",
                "content": f"""
Original Prompt:
{prompt}

Diagnosis:
{diagnosis}

Return improved prompt only.
"""
            }
        ])


    def fix_output(self, output: str, diagnosis: str):

        return call_llm([
            {
                "role": "system",
                "content": "Fix broken backend output."
            },
            {
                "role": "user",
                "content": f"""
Output:
{output}

Issue:
{diagnosis}

Return corrected full output.
"""
            }
        ])