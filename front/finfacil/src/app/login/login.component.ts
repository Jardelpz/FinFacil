import { Component, OnInit } from '@angular/core';
import { UserService } from '../user.service';
import { UserModel } from '../register/user.model';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  user: UserModel = new UserModel()
  constructor(private userService: UserService, private router: Router) { }

  ngOnInit() {
  }

  verificaLogin(){
    this.userService.loginUser(this.user).subscribe(dado =>{
      console.log(dado)
    }, erro =>{
      this.router.navigateByUrl('/login')
    })
  }

}
