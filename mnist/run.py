import ems

def main():
  # Define list of configuration, each configuration is a configuration files
  search_space = [ 
  { "params":{"a": 0, "b": 1,}, }, 
  { "params":{"a": -3, "b": 1,}, },
  { "params":{"a": -2, "b": 5,}, },
  ]
  pipeline_dag = "pipeline_v1"

  # Run experiments
  ems.run_configurations(
    pipeline_dag = pipeline_dag,
    search_space = search_space,
  )
  return

if __name__ == "__main__":
  main()

