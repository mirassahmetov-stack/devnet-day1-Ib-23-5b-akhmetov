# Day 3 Report — Lab 4.5.5 + Auto-check artifacts

## 1) Student
- Name: ...
- Group: ...
- Token: ...
- Repo: ...



## 3) Artifacts checklist
artifacts/day3/books_before.json: Yes

artifacts/day3/books_sorted_isbn.json: Yes

artifacts/day3/mybook_post.json: Yes

artifacts/day3/books_by_me.json: Yes

artifacts/day3/add100_report.json: Yes

artifacts/day3/postman_collection.json: Yes

artifacts/day3/postman_environment.json: Yes

artifacts/day3/curl_get_books.txt: Yes

artifacts/day3/curl_get_books_isbn.txt: Yes

artifacts/day3/curl_get_books_sorted.txt: Yes

artifacts/day3/summary.json: Yes

## 4) Command outputs (paste exact)
### 4.1 Script run
{
  "schema_version": "3.1",
  "generated_utc": "2026-03-19T15:37:10.573753+00:00",
  "student": {
    "token": "D1-IB-23-5b-01-1A3F",
    "token_hash8": "4b0b5022",
    "name": "Akhmetov",
    "group": "IB-23-5b"
  },
  "lab": {
    "apihost": "http://library.demo.local",
    "must_use": {
      "login_endpoint": "http://library.demo.local/api/v1/loginViaBasic",
      "books_endpoint": "http://library.demo.local/api/v1/books",
      "api_key_header": "X-API-KEY"
    }
  },
  "artifacts_sha256": {
    "books_before": "e9d34fda886ea13e48f880ed70831f5548107833a76bb9f8888b88bb5c979458",
    "books_sorted_isbn": "93934547f1e3d0d592639533661497ca2eb6a8b60073b0bfd7fecc086edf0d6b",
    "mybook_post": "05b33fa60b87fd07fbe72bdc6f1ab8a7c09ed0cd50007deacaeccf275ef038cd",
    "books_by_me": "c649076dd495449cf642b1715830621d453fd550678ad07da2ee3086e8c08e0e",
    "add100_report": "a6b0dd5df259a30119235a1fe309d36585cb1d541e6b478291efe5a44292b0e6",
    "postman_collection": "21527dec4c4e33342af25f064c0ac2953ab3d0502e2440c08aac1fbcf28fae06",
    "postman_environment": "0cb91514ee6ed1fe4139664643382ea06966e11e010b0b98e845dcfa3be3fc3e",
    "curl_get_books": "de64bae22fde03848fbeb14e2a6c661cf7e9eed12f29b574d596224bf5bf6bf9",
    "curl_get_books_isbn": "ee1093008a5d89a75d9aaf8a2c8a7987c8841bce0c4028d02d32e78f083fb227",
    "curl_get_books_sorted": "6e87e9da9e47b139ee6633b979ddefac161bd7ee3006a66118067b2b866bcef5"
  },
  "validation": {
    "must_have_mybook_title_contains_token_hash8": true,
    "must_have_added_100": true
  }
}

### 4.2 Tests
.                                                                    [100%]
1 passed in 0.34s

