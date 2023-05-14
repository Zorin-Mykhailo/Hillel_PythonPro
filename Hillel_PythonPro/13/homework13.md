1. Authentication
  
  1.1. Type??? OAuth???  
  1.2. No password recovery  
  1.3. Auth flow (registration, login, logout)  
  1.4. Password recovery? Maybe...  
  1.5. Password valodation: NIST (8+, upper, lower, num, special char)
  
2. Roles: [User, Manager, Admin(God?)]

3. Users
  3.1. Username is unique? :heavy_check_mark:

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
