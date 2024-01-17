import asyncio
from pathlib import Path

from library.boilerplate import API
from novelai_api.ImagePreset import ImageModel, ImagePreset, ImageResolution, UCPreset
import random
import ulid
import os

class GenerateConfig:

    def __init__(self, n_samples:int=3, negative_prompt:str=None, seed:int=random.randint(0,255)) -> None:
        self.n_samples = n_samples
        self.negative_prompt = negative_prompt
        self.seed = seed
        pass

class ImageGenerate:
    
    def __init__(self, generateConfig:GenerateConfig=None) -> None:
        if generateConfig is None:
            self.generateConfig = GenerateConfig()
        else:
            self.generateConfig = generateConfig
        pass

    # async def generate(self, input_context:str) -> [bytes|str]:

    #     async with API() as api_handler:
    #         api = api_handler.api
    #         preset = ImagePreset()
    #         preset.seed = self.generateConfig.seed
    #         preset.n_samples = self.generateConfig.n_samples
    #         preset.uc = self.generateConfig.negative_prompt

    #         results = []
    #         async for _, img in api.high_level.generate_image(input_context, ImageModel.Anime_Full, preset):
    #             if isinstance(img, bytes) :
    #                 print("img is bytes")
    #                 results.append(img)
    #             else:
    #                 print("str or etc")
                
    #         # print(results)
    #         return results
    #     pass

    async def generate_files(self, input_context:str) -> [str]:

        async with API() as api_handler:
            api = api_handler.api
            preset = ImagePreset()
            preset.seed = self.generateConfig.seed
            preset.n_samples = self.generateConfig.n_samples
            preset.uc = self.generateConfig.negative_prompt

            results = []
            async for _, img in api.high_level.generate_image(input_context, ImageModel.Anime_Full, preset):
                if isinstance(img, bytes) :
                    print("img is bytes xx")
                    filename = self._write_file(img)
                    results.append(filename)
                else:
                    print("str or etc")
                
            # print(results)
            return results
        pass

    def _write_file(self, data:bytes) -> str:
        try:
            id = ulid.new()
            dir = os.getenv("STORAGE_PATH")
            filename = f"{id}.jpg"
            path = os.path.join(dir, filename)
            print("path:{path}")
            with open(path, "wb") as f:
                f.write(data)
                f.flush()

            return path
        except Exception as e:
            print(e)
            return None

