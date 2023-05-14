# Support database relational schema



```mermaid
erDiagram

  UserRole {
    int Id PK
    String RoleName
  }
  
  User {
    int Id PK
    String UserName
    String FirstName
    String LastName
    int RoleId FK
  }
  
  Request {
    int Id PK
    String Theme "Only 75 characters are allowed"
    int AuthorId
    int ManagerId
  }
  
  Message {
    int Id PK
    int RequestId
    String Text
  }
  
  Request ||--|{ Message : contains
  Request ||--|{ Message : contains
  
```

---

[About Mermaid entity relationship diagrams](https://mermaid.js.org/syntax/entityRelationshipDiagram.html)

Conventions of relationships between entities:

```mermaid
erDiagram

ExactlyOne {  
}

ZeroOrOne {  
}

ZeroOrMore {
}

OneOrMore {
}

ExactlyOne ||--o| ZeroOrOne : "to"
ExactlyOne ||--o{ ZeroOrMore : "to"
ExactlyOne ||--|{ OneOrMore : "to"
  
```
