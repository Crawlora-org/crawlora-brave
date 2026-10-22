use crawlora_brave::{BraveSearchParams, Client, ModelBraveSearchResponseDoc};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = std::env::var("CRAWLORA_API_KEY")?;
    let client = Client::new(api_key)?;
    let response = client
        .brave
        .search(BraveSearchParams {
            q: Some("open source web crawler".to_owned()),
            ..Default::default()
        })
        .await?;
    let data: ModelBraveSearchResponseDoc = response.into_json()?;
    println!("{data:#?}");
    Ok(())
}
