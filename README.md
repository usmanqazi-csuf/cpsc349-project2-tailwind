# Getting started with Project 2

Install [q][1] in order to run SQL directly on TSV files:

```shell-session
$ sudo apt update
$ sudo apt install python3-q-text-as-data
```

[Fork][2] the GitHub [cpsc349-project2][3] repository, then [clone][4]
your forked repository locally:

```shell-session
$ git clone https://github.com/USERNAME/cpsc349-project2.git
```

Download the [Unsplash Lite dataset][5] and extract some pet photos:

``` shell-session
$ cd cpsc349-project2/unsplash
$ make
```

Install and start [Eleventy][6], [Browsersync][7], and the
[Tailwind CLI][8]:

```shell-session
$ cd ..
$ npm install
$ npm start

```

Open the [newly generated site][9].

To publish the site, enable [GitHub Pages][10] for the repository,
set the source for the site to the `/docs` folder in the main branch,
then run the publish script, commit the update, and push the repository:

```shell-session
$ npm run publish
$ git add docs
$ git commit -m 'Publishing site updates'
$ git push origin main

```

To check the deployment results, click the
[Environments](../../deployments) link on the right-hand side of the
page.


[1]: https://harelba.github.io/q/
[2]: https://docs.github.com/en/get-started/quickstart/fork-a-repo
[3]: https://github.com/ProfAvery/cpsc349-project2
[4]: https://docs.github.com/en/get-started/quickstart/fork-a-repo#cloning-your-forked-repository
[5]: https://github.com/unsplash/datasets
[6]: https://www.11ty.dev/
[7]: https://browsersync.io/
[8]: https://tailwindcss.com/docs/installation#using-tailwind-cli
[9]: http://localhost:3000/
[10]: https://guides.github.com/features/pages/
