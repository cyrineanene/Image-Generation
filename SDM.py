import torch
from diffusers import StableDiffusionPipeline

class SDM:
    def __init__(self, auth_token, modelid = "CompVis/stable-diffusion-v1-4"):
        self.modelid = modelid
        self.stable_diffusion_model = StableDiffusionPipeline.from_pretrained(self.modelid, torch_dtype=torch.float16, use_auth_token=auth_token)

    def generate(self, prompt): 
        image = self.stable_diffusion_model(prompt).images[0]
        return image