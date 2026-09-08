# IP List Filter
A simple Python script that removes blocked/flagged IP addresses from an allowed-list file.

This was written as a Python practice project — a small, self-contained exercise for working with file I/O, list operations.

## When this is useful
- Maintaining a network firewall or access-control allowlist, where IPs need to be periodically revoked.
- Any situation where you keep a "master list" in a text file and need to remove a batch of entries found in a separate "to remove" file.
- As a template for basic file-read → filter → file-write workflows in Python.

## What it does
1. Reads a list of currently allowed IPs from a text file.
2. Reads a list of IPs that need to be removed.
3. Filters out any IP found in the removal list.
4. Writes the result to a new file.

## Files

```
ip-list-filter/
├── data/
│   ├── allowed_list.txt     # currently allowed IPs
│   ├── to_remove_list.txt   # IPs to remove
│   └── updated_list.txt     # output (generated)
├── README.md
├── update_ip.py
```
