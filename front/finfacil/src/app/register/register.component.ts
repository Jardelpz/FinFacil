import { Component, OnInit } from '@angular/core';
import { UserModel } from './user.model';
import { UserService } from '../user.service';
import { RouterLink, Router  } from '@angular/router';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})

export class RegisterComponent implements OnInit {

  user: UserModel = new UserModel()
  constructor(private userService: UserService, private router: Router) { }
  
  ngOnInit() {
  }

  addUser(){
    this.userService.postUser(this.user).subscribe(dado => {
      console.log(dado)
    }, err =>{
      this.router.navigateByUrl('/register')
      console.log("Erro ao criar usuário")
    })
  }

}
