import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { UserModel } from './register/user.model';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(private http: HttpClient) {  }
  user: UserModel = new UserModel()
  postUser(user: UserModel): Observable<any>{
    return this.http.post("http://localhost:5000/register", user)
  }
  loginUser(user: UserModel): Observable<any>{
    return this.http.post("http://localhost:5000/login", user)
  }

}
