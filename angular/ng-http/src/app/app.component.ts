import {Component, OnInit} from '@angular/core'
import {Todo, TodosService} from "./todos.service";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {

  todos: Todo[] = [];
  loading = false;
  todoTitle = '';

  constructor(private todosService: TodosService) {
  }

  ngOnInit() {
    this.fetchTodos();
  }

  addTodo() {
    if (!this.todoTitle.trim()) {
      return;
    }
    const newTodo: Todo = {
      title: this.todoTitle,
      completed: false,
    };

    this.todosService.addTodo(newTodo)
      .subscribe((todo) => {
        this.todos.push(todo);
        this.todoTitle = '';
      });
  }

  fetchTodos() {
    this.loading = true;
    this.todosService.fetchTodos()
      .subscribe((todos) => {
        console.log('Response', todos);
        this.todos = todos;
        this.loading = false;
      });
  }

  removeTodo(id: number) {
    this.todosService.removeTodo(id)
      .subscribe((resp) => {
        this.todos = this.todos.filter((t) => (t.id !== id));
      });
  }
}
