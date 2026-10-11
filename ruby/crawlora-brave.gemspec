require_relative "lib/crawlora/brave/version"

Gem::Specification.new do |spec|
  spec.name = "crawlora-brave"
  spec.version = Crawlora::Brave::VERSION
  spec.summary = "Brave Search API client for Crawlora (5 endpoints)"
  spec.description = "Ruby client for Crawlora's hosted Brave Search API. Covers web, news, image, and video search plus query suggestions across 5 endpoints."
  spec.authors = ["Crawlora"]
  spec.license = "MIT"
  spec.required_ruby_version = ">= 2.6"
  spec.files = Dir["lib/**/*.rb", "README.md", "CHANGELOG.md", "LICENSE"]
  spec.require_paths = ["lib"]
  spec.homepage = "https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=brave-ruby-homepage"
  spec.metadata = { "source_code_uri" => "https://github.com/Crawlora-org/crawlora-brave", "documentation_uri" => "https://github.com/Crawlora-org/crawlora-brave/blob/main/ruby/README.md", "rubygems_mfa_required" => "true" }

end
