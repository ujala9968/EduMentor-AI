def summarize_text(text):
    """
    Very simple summarizer:
    Returns the first sentence from the text.
    """
    sentences = text.split(".")
    return sentences[0].strip() + "." if len(sentences) > 0 else "Not enough data"
