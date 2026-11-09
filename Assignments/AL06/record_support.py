"""Supplied per-record validation; students implement selection and both traversals."""


def validate_node(node):
    """Reject malformed records without selecting eligible entries or totaling them."""
    if not isinstance(node, dict) or not isinstance(node.get("name"), str):
        raise ValueError("Every record needs a name and an entry/group dictionary.")
    if node.get("type") == "entry":
        amount = node.get("amount")
        if type(amount) is not int or amount < 0:
            raise ValueError("Amounts must be nonnegative integers; booleans are not amounts.")
        if not isinstance(node.get("status"), str) or not node["status"]:
            raise ValueError("Every entry needs a nonempty status string.")
    elif node.get("type") == "group":
        if not isinstance(node.get("items"), list):
            raise ValueError("A group needs an items list, which may be empty.")
    else:
        raise ValueError("Record type must be entry or group.")
