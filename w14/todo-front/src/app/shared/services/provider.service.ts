import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { MainService } from './main.service';
import { ITasks, ITaskList, IAuthResponse } from '../models/models';

@Injectable({
  providedIn: 'root'
})

export class ProviderService extends MainService{

  constructor(http: HttpClient) { 
    super(http);
  }

  getTaskList(): Promise<ITaskList[]>{
    return this.get('http://localhost:8000/api/tasklist/', {});
  }

  getTasks(tasklist: ITaskList): Promise<ITasks[]> {
    return this.get(`http://127.0.0.1:8000/api/tasklist/${tasklist.id}/tasks/`, {});
  }

  createTaskList(name: any): Promise<ITaskList> {
    return this.post('http://127.0.0.1:8000/api/tasklist/', {
      name: name
    });
  }

  updateTaskList(tasklist: ITaskList): Promise<ITaskList> {
    return this.put(`http://127.0.0.1:8000/api/tasklist/${tasklist.id}/`, {
      name: tasklist.name
    });
  }

  deleteTaskList(id: number): Promise<any> {
    return this.delet(`http://127.0.0.1:8000/api/tasklist/${id}/`, {});
  }

  auth(login: string, password: string): Promise<IAuthResponse> {
    return this.post('http://localhost:8000/api/login/', {
      username: login,
      password: password
    });
  }

  logout(): Promise<any> {
    return this.post('http://localhost:8000/api/logout/', {});
  }
}
