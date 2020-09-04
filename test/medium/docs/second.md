# Second page
Testing special cases

## Wrong diagram

```mermaid
graph FG
A[Client] 
```

## Correct

```mermaid
graph TD
A[Client] --> B[Load Balancer]
```

## Other

```mermaid
graph TD
  A[Client] --> B[Load Balancer]
  B --> C[Server01]
  B --> D[Server02]
```
