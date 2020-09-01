from amazon.paapi import AmazonAPI

# US
access_key_US = "AKIAJTVOWFPSQHRZUJCA"
secret_key_US = "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"
partner_tag_US = "clouds056-20"

# JP
access_key_JP = "AKIAISMYWF6AZ2TRPGCQ"
secret_key_JP = "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"
partner_tag_JP = "cloudsjp04-22"

amazon = AmazonAPI(access_key_JP, secret_key_JP, partner_tag_JP, "JP")

product = amazon.get_product('7b3e545a3ba19782f8a732e8a721b574')

print(product.title)