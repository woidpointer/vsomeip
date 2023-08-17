namespace :conan do
  task :source do
    sh 'conan source .'
  end

  task :install do
    cmd  = ['conan']
    cmd << 'install .'

    sh cmd.join(' ')
  end

  task :build do
    cmd = ['conan']
    cmd << 'build .'

    sh cmd.join(' ')
  end

  task :package do
    cmd = ['conan']
    cmd << 'export-pkg .'

    sh cmd.join(' ')
  end

  task :create do
    cmd = ['conan']
    cmd << 'create .'

    sh cmd.join(' ')
  end
end
