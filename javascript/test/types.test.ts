import { BraveClient } from "../src/index.js";

const client = new BraveClient({ apiKey: "test-key" });
void client.images({"q": "sample"});
void client.request("brave-images", {"q": "sample"});
const streamResponse: Promise<Response> = client.request("brave-images", {"q": "sample"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("brave-images", {"q": "sample"}, { responseType: "stream" });
const directStream: Promise<Response> = client.images({"q": "sample"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("brave-images", {"q": "sample", "offset": 1, "count": 1, "country": "all", "lang": "de-de"}, { responseType: "text" });
const rawText: Promise<string> = client.request("brave-images", {"q": "sample"}, { responseType: "text" });
void rawText;



// @ts-expect-error The selected operation requires its documented params.
void client.images();
