def extract_text_from_medium(url):
    import requests
    from bs4 import BeautifulSoup
    # Set headers to imitate a web browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    # Send a GET request to the website with headers
    response = requests.get(url, headers=headers)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the main content container
    main_content = soup.find('article')

    # Find all paragraph elements within the main content
    paragraphs = main_content.find_all('p')

    # Extract the text from the paragraphs
    extracted_text = ' '.join([p.get_text() for p in paragraphs])

    # Remove any leading or trailing whitespace
    extracted_text = extracted_text.strip()

    return extracted_text