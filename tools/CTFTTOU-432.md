# CTFTTOU-432 — AzCopy and az storage (data plane)

> **Tool ID:** `CTFTTOU-432`  
> **Related techniques/counters:** CTFTTE-CLD-001, CTFTCTE-CLD-001, CTFTTE-CLD-011, CTFTCTE-CLD-011

## Description

The storage **data plane** clients. The distinction that matters in a challenge is that a control-plane
grant and a data-plane grant are separate checks: an identity can list storage accounts without being able
to read a single blob, and a signed URL can read one object with no identity at all.

- **`az storage`** — listing, upload, download and metadata, with three authentication modes that a
  challenge will make you choose between: account key, connection string, or `--auth-mode login` (identity).
- **AzCopy** — the transfer engine, and the most forgiving way to exercise a signed URL: it accepts a URL
  whose query string carries the grant, so a leaked signature becomes a listing or a download directly.

Both speak the same REST API, which is also usable with a bare HTTP client when the response headers are
the evidence.

## URL

- <https://github.com/Azure/azure-storage-azcopy>
- <https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction>

## Installation

```bash
# AzCopy v10, single static binary
curl -sL https://aka.ms/downloadazcopy-v10-linux | tar -xz
sudo install azcopy_linux_amd64_*/azcopy /usr/local/bin/ && azcopy --version

# az storage ships with the CLI; the data-plane plugin may need to be added
az extension add --name storage-preview 2>/dev/null || true
```

## Usage

```bash
# identity-based (both planes must grant access)
az storage container list --account-name ACCT --auth-mode login -o table
az storage blob list --account-name ACCT -c CONTAINER --auth-mode login -o table
az storage blob download --account-name ACCT -c CONTAINER -n flag.txt -f - --auth-mode login

# signed URL: the grant is the query string, no identity involved
azcopy list "https://ACCT.blob.core.windows.net/CONTAINER?<SAS>"
azcopy cp "https://ACCT.blob.core.windows.net/CONTAINER/flag.txt?<SAS>" ./flag.txt

# raw data-plane call, when the API version or headers matter
curl -s "https://ACCT.blob.core.windows.net/CONTAINER?restype=container&comp=list&<SAS>"
curl -s -H "x-ms-version: 2021-08-06" "https://ACCT.blob.core.windows.net/CONTAINER?restype=container&comp=list"
```

Pitfalls: a `403` with `AuthenticationFailed` on a signed URL is usually a signature or clock problem, not
a policy one; `PublicAccessNotPermitted` means the account forbids anonymous access (a signature is still
usable); a listing that returns only a handful of entries is paginated (`NextMarker`); `--auth-mode login`
against a storage account whose network rules exclude you fails before authorisation is evaluated.

## Related Techniques

CTFTTE-CLD-001, CTFTCTE-CLD-001, CTFTTE-CLD-011, CTFTCTE-CLD-011

## References

- [AzCopy documentation](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10)
- [Shared access signatures](https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview)
- [Blob service REST API](https://learn.microsoft.com/en-us/rest/api/storageservices/blob-service-rest-api)
