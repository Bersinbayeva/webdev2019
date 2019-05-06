import { Component, Input, OnInit } from '@angular/core';
import { ProviderService } from '../shared/services/provider.service';
import { ITaskList, ITasks } from '../shared/models/models';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})

export class MainComponent implements OnInit {

  public tasklists: ITaskList[] = [];
  public tasks: ITasks[] = [];
  public name: any = '';

  public isLogged = false;

  public login: any = '';
  public password: any = '';

  constructor(private provider: ProviderService) { }

  ngOnInit() {

    const token = localStorage.getItem('token');
    if (token) {
      this.isLogged = true;
    }
    

    if (this.isLogged) {
      // console.log(token);
      this.getTaskList();
    }

  }

  getTaskList() {
    this.provider.getTaskList().then(res => {
      this.tasklists = res;
    });
  }

  getTasks(taskList: ITaskList){
    this.provider.getTasks(taskList).then(res => {
      console.log(res);
      this.tasklists = res;
    });
  }

  updateTaskList(t: ITaskList){
    this.provider.updateTaskList(t).then(res => {
      console.log(t.name + ' updated');
    });
  }

  deleteTaskList(t: ITaskList){
    this.provider.deleteTaskList(t.id).then(res => {
      console.log(t.name + ' deleted');
      this.provider.getTaskList().then(res => {
        this.tasklists = res;
      });
    });
  }

  createTaskList(){
    if(this.name !== ''){
      this.provider.createTaskList(this.name).then(res => {
        this.name = '';
        this.tasklists.push(res);
      });
    }
  }

  auth() {
    if (this.login !== '' && this.password !== '') {
      this.provider.auth(this.login, this.password).then(res => {
        localStorage.setItem('token', res.token);
        this.isLogged = true;
        this.getTaskList();
      });
    }
  }

  logout() {
    this.provider.logout().then(res => {
      this.isLogged = false;
      localStorage.clear();
    });
  }

}
