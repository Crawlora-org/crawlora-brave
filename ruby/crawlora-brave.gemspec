require_relative "lib/crawlora/brave/version"

Gem::Specification.new do |spec|
  spec.name = "crawlora-brave"
  spec.version = Crawlora::Brave::VERSION
  spec.summary = "Brave Search client for the Crawlora hosted API"
  spec.description = "Credential-free Brave Search API access through Crawlora's hosted service."
  spec.authors = ["Crawlora"]
  spec.license = "MIT"
  spec.required_ruby_version = ">= 2.6"
  spec.files = Dir["lib/**/*.rb", "README.md", "CHANGELOG.md", "LICENSE"]
  spec.require_paths = ["lib"]
  spec.homepage = "https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=brave-ruby-homepage"
  spec.metadata = { "source_code_uri" => "https://github.com/Crawlora-org/crawlora-brave", "documentation_uri" => "https://github.com/Crawlora-org/crawlora-brave/blob/main/ruby/README.md", "rubygems_mfa_required" => "true" }

end
