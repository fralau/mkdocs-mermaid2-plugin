# Second page
Testing special cases

## Wrong diagram

```mermaid
graph FG
A[Client] 
```

## First Note (collapsible open)

???+ note "Collapsable but open"
    ```mermaid
    graph TD
    A[Client] --> B[Load Balancer]
    ```

## Second note (collapsed)

**This doesn't work (known bug).**
On Chrome/Safari it appears as a dot. On Firefox, it appears as
a mermaid error.

???- note "Collapsed"
    ```mermaid
    graph TD
    A[Client] --> B[Load Balancer]
    ```
    Hello