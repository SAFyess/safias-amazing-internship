# flux1devfp8 

Created by: `Black Forest Labs`

I asked the model `What are you capable of doing?` and it replied:

Completions exception: litellm.BadRequestError: OpenAIException - Error code: 400 - {'detail': "Error code: 404 - {'detail': 'Not Found'}"}
[ERROR PYTHON]: Bad request: litellm.BadRequestError: OpenAIException - Error code: 400 - {'detail': "Error code: 404 - {'detail': 'Not Found'}"}
[ERROR PYTHON TRACEBACK]: Traceback (most recent call last):
  File "/home/dmesg/miniconda3/envs/nai/lib/python3.9/site-packages/nearai/agents/agent.py", line 175, in run_python_code
    exec(self.code, agent_namespace)
  File "/tmp/agent_f594b4e7bfc44fc2947a800d3d6d3cf7/agent.py", line 17, in <module>
    run(env)
  File "/tmp/agent_f594b4e7bfc44fc2947a800d3d6d3cf7/agent.py", line 12, in run
    result = env.completion([prompt] + env.list_messages())
  File "/home/dmesg/miniconda3/envs/nai/lib/python3.9/site-packages/nearai/agents/environment.py", line 1362, in completion
    raw_response = self.completions(messages, model, **kwargs)
  File "/home/dmesg/miniconda3/envs/nai/lib/python3.9/site-packages/nearai/agents/environment.py", line 1179, in completions
    return self._run_inference_completions(messages, model, False, **kwargs)
  File "/home/dmesg/miniconda3/envs/nai/lib/python3.9/site-packages/nearai/agents/environment.py", line 488, in _run_inference_completions
    completions = client.completions(
  File "/home/dmesg/miniconda3/envs/nai/lib/python3.9/site-packages/nearai/shared/inference_client.py", line 156, in completions
    raise ValueError(f"Bad request: {e}") from None
ValueError: Bad request: litellm.BadRequestError: OpenAIException - Error code: 400 - {'detail': "Error code: 404 - {'detail': 'Not Found'}"}