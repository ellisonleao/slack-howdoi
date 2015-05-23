# slack-howdoi

A slack integration for the awesome [howdoi](https://github.com/gleitz/howdoi) library.
Inspired by [https://github.com/karan/slack-overflow](https://github.com/karan/slack-overflow)

## Usage

From any Slack channel, just type `/howdoi [search terms]`. The questions will be shown on the same channel visible just to you.

## Integrate with your team

1. Go to your channel
2. Click on **Configure Integrations**.
3. Scroll all the way down to **DIY Integrations & Customizations section**.
4. Click on **Add** next to **Slash Commands**.
  - Command: `/howdoi`
  - URL: `http://so.goel.io/overflow`
  - Method: `POST`
  - For the **Autocomplete help text**, check to show the command in autocomplete list.
    - Description: `Howdoi slack integration`
    - Usage hint: `[search terms]`
  - Descriptive Label: `Howdoi search`

## Developing

```python
# Install python dependencies
$ pip install -r requirements.txt

# Start the server
$ DEBUG=True python app.py
```

## Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)


## Contributing

- Please use the [issue tracker](https://github.com/ellisonleao/slack-howdoi/issues) to report any bugs or file feature requests.
