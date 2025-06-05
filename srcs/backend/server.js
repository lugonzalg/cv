const express = require('express');
const cors = require('cors');
const app = express();
const PORT = process.env.PORT || 3001;

app.use(cors());
app.use(express.json());

// Mock projects
const projects = [
  {
    id: 1,
    name: 'Project One',
    description: 'First mock project description.',
    skills: ['Vue', 'Node', 'Docker'],
    repo: 'https://github.com/example/project-one'
  },
  {
    id: 2,
    name: 'Project Two',
    description: 'Second mock project description.',
    skills: ['Python', 'Flask'],
    repo: 'https://github.com/example/project-two'
  }
];

app.get('/api/projects', (_req, res) => {
  res.json(projects);
});

app.listen(PORT, () => {
  console.log(`Backend listening on port ${PORT}`);
});
