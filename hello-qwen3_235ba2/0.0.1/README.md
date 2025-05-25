# qwen3_235ba2

Created by: `Alibaba Cloud`

---
I asked the model `What are you capable of doing?` and it replied:

Traceback (most recent call last):
  File "/home/dmesg/miniconda3/envs/nai/bin/nearai", line 8, in <module>
    sys.exit(main())
  File "/home/dmesg/miniconda3/envs/nai/lib/python3.9/site-packages/nearai/cli.py", line 1277, in main
    fire.Fire(CLI)
  File "/home/dmesg/miniconda3/envs/nai/lib/python3.9/site-packages/fire/core.py", line 143, in Fire
    component_trace = _Fire(component, args, parsed_flag_args, context, name)
  File "/home/dmesg/miniconda3/envs/nai/lib/python3.9/site-packages/fire/core.py", line 477, in _Fire
    component, remaining_args = _CallAndUpdateTrace(
  File "/home/dmesg/miniconda3/envs/nai/lib/python3.9/site-packages/fire/core.py", line 693, in _CallAndUpdateTrace
    component = fn(*varargs, **kwargs)
  File "/home/dmesg/miniconda3/envs/nai/lib/python3.9/site-packages/nearai/cli.py", line 827, in interactive
    last_message_id = self._task(
  File "/home/dmesg/miniconda3/envs/nai/lib/python3.9/site-packages/nearai/cli.py", line 959, in _task
    LocalRunner(str(local_path), agent, thread.id, run.id, auth, params)
  File "/home/dmesg/miniconda3/envs/nai/lib/python3.9/site-packages/nearai/agents/local_runner.py", line 15, in __init__
    run_with_environment(agents, auth, thread_id, run_id, additional_path=path, params=params)
  File "/home/dmesg/miniconda3/envs/nai/lib/python3.9/site-packages/nearai/aws_runner/service.py", line 395, in run_with_environment
    environment_run = start_with_environment(agents, auth, thread_id, run_id, additional_path, params, print_system_log)
  File "/home/dmesg/miniconda3/envs/nai/lib/python3.9/site-packages/nearai/aws_runner/service.py", line 380, in start_with_environment
    env.add_agent_start_system_log(agent_idx=0)
  File "/home/dmesg/miniconda3/envs/nai/lib/python3.9/site-packages/nearai/agents/environment.py", line 889, in add_agent_start_system_log
    model = self.get_model_for_inference(agent.model)
  File "/home/dmesg/miniconda3/envs/nai/lib/python3.9/site-packages/nearai/agents/environment.py", line 471, in get_model_for_inference
    _, model_for_inference = client.provider_models.match_provider_model(model, provider)
  File "/home/dmesg/miniconda3/envs/nai/lib/python3.9/site-packages/nearai/shared/provider_models.py", line 109, in match_provider_model
    raise ValueError(f"Model {namespaced_model} not present in provider models {self.provider_models}")
ValueError: Model qwen3_235ba2 not present in provider models {NamespacedName(name='qwq32b', namespace=''): {'fireworks': 'fireworks::accounts/fireworks/models/qwq-32b'}, NamespacedName(name='srlfinetune0417debug', namespace='instacart'): {'fireworks': 'fireworks::accounts/instacart/models/srl-finetune-0417-debug'}, NamespacedName(name='flux1devfp8', namespace=''): {'fireworks': 'fireworks::accounts/fireworks/models/flux-1-dev-fp8'}, NamespacedName(name='llama4maverickinstructbasic', namespace=''): {'fireworks': 'fireworks::accounts/fireworks/models/llama4-maverick-instruct-basic'}, NamespacedName(name='qwen3_30ba3b', namespace=''): {'fireworks': 'fireworks::accounts/fireworks/models/qwen3-30b-a3b'}, NamespacedName(name='deepseekr1basic', namespace=''): {'fireworks': 'fireworks::accounts/fireworks/models/deepseek-r1-basic'}, NamespacedName(name='llamaguard3_8b', namespace=''): {'fireworks': 'fireworks::accounts/fireworks/models/llama-guard-3-8b'}, NamespacedName(name='qwen2p5vl32binstruct', namespace=''): {'fireworks': 'fireworks::accounts/fireworks/models/qwen2p5-vl-32b-instruct'}, NamespacedName(name='llama4scoutinstructbasic', namespace=''): {'fireworks': 'fireworks::accounts/fireworks/models/llama4-scout-instruct-basic'}, NamespacedName(name='qwen2vl72binstruct', namespace=''): {'fireworks': 'fireworks::accounts/fireworks/models/qwen2-vl-72b-instruct'}, NamespacedName(name='firesearchocr6', namespace=''): {'fireworks': 'fireworks::accounts/fireworks/models/firesearch-ocr-v6'}, NamespacedName(name='deepseek3', namespace=''): {'fireworks': 'fireworks::accounts/fireworks/models/deepseek-v3'}, NamespacedName(name='llama3p1_8binstruct', namespace=''): {'fireworks': 'fireworks::accounts/fireworks/models/llama-v3p1-8b-instruct'}, NamespacedName(name='llama3p1_70binstruct', namespace=''): {'fireworks': 'fireworks::accounts/fireworks/models/llama-v3p1-70b-instruct'}, NamespacedName(name='deepseek3_0324', namespace=''): {'fireworks': 'fireworks::accounts/fireworks/models/deepseek-v3-0324'}, NamespacedName(name='qwen3_235ba22b', namespace=''): {'fireworks': 'fireworks::accounts/fireworks/models/qwen3-235b-a22b'}, NamespacedName(name='llama3p3_70binstruct', namespace=''): {'fireworks': 'fireworks::accounts/fireworks/models/llama-v3p3-70b-instruct'}, NamespacedName(name='deepseekr1', namespace=''): {'fireworks': 'fireworks::accounts/fireworks/models/deepseek-r1'}, NamespacedName(name='dobbyunhingedllama3_370bnew', namespace='sentientfoundation'): {'fireworks': 'fireworks::accounts/sentientfoundation/models/dobby-unhinged-llama-3-3-70b-new'}, NamespacedName(name='flux1schnellfp8', namespace=''): {'fireworks': 'fireworks::accounts/fireworks/models/flux-1-schnell-fp8'}, NamespacedName(name='r1_1776', namespace='perplexity'): {'fireworks': 'fireworks::accounts/perplexity/models/r1-1776'}, NamespacedName(name='llama3p1_405binstructlong', namespace=''): {'fireworks': 'fireworks::accounts/fireworks/models/llama-v3p1-405b-instruct-long'}, NamespacedName(name='llama3p1_405binstruct', namespace=''): {'fireworks': 'fireworks::accounts/fireworks/models/llama-v3p1-405b-instruct'}, NamespacedName(name='mixtral8x22binstruct', namespace=''): {'fireworks': 'fireworks::accounts/fireworks/models/mixtral-8x22b-instruct'}, NamespacedName(name='qwen2p5_72binstruct', namespace=''): {'fireworks': 'fireworks::accounts/fireworks/models/qwen2p5-72b-instruct'}}