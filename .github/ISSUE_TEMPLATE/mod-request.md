---
name: Mod request
about: Suggest an mod for this modpack
title: ''
labels: mod
assignees: ''

---

body:
- type: markdown
  attributes:
    value: |
      Before you request a mod, [please search](https://github.com/lalamapaka/faster-than-light/issues) if it has already been requested.

- type: input
  attributes:
    label: Mod name
  validations:
    required: true

- type: input
  attributes:
    label: Link to the mod
time to be included.
  validations:
    required: true

- type: textarea
  attributes:
    label: What does it do
    description: What does the mod do. 
  validations:
    required: true

- type: textarea
  attributes:
    label: Why should it be in the Faster than light
    description: How can everyone profit from the mod while keeping the experience "vanilla-ish"?
  validations:
    required: true

- type: textarea
  attributes:
    label: Why shouldn't it be in the modpack
    description: Don't forget to include any downsides of the mod, you know every mod has some.
    placeholder: |
      Examples: Still in alpha, ...
  validations:
      required: true

- type: dropdown
  attributes:
    label: Categories
    description: Select all that match the mod.
    multiple: true
    options:
      - Performance improvements
      - Graphics improvements
      - New feature
      - Works like Optifine/Forge/etc
      - Fixes a bug
      - Replaces an already existing mod
  validations:
    required: true
    
- type: textarea
  attributes:
    label: Other details
    description: Anything else you want to say to convince me?
  validations:
    required: false

[] It's compatible with the fabric mod loader.
[] It supports the latest minecraft release.
