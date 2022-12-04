#!/bin/bash

blacklist=("openai.com" "www.openai.com" "api.openai.com" "blog.openai.com" "docs.openai.com" "forum.openai.com" "jobs.openai.com" "research.openai.com" "status.openai.com" "support.openai.com" "team.openai.com" "beta.openai.com" "chat.openai.com")

for domain in "${blacklist[@]}"; do
  iptables -A OUTPUT -p tcp -d $domain -j DROP
done
