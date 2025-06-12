from nsfw_detector import predict
import asyncio
import os
import aiohttp

model = predict.load_model("nsfw_detector/nsfw_model.h5")  # Downloaded automatically

async def is_nsfw_image(file_path: str, threshold: float = 0.7) -> bool:
    predictions = predict.classify(model, file_path)
    if not predictions:
        return False

    for _, scores in predictions.items():
        if scores.get("porn", 0) > threshold or scores.get("hentai", 0) > threshold or scores.get("sexy", 0) > threshold:
            return True
    return False

async def download_and_check(app, message, file_path="temp.jpg") -> bool:
    try:
        await app.download_media(message, file_path)
        result = await is_nsfw_image(file_path)
        os.remove(file_path)
        return result
    except Exception as e:
        print(f"[NSFW DETECTION ERROR] {e}")
        return False
