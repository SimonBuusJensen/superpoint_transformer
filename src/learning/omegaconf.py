from omegaconf import OmegaConf

OmegaConf.register_new_resolver("eval", eval)

yaml_data = """
ten: 10
twenty: 20
result: ${eval:' ${ten} + ${twenty}*0.5'}
"""

cfg = OmegaConf.create(yaml_data)

print(cfg.result)  # 30