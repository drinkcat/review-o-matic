from reviewer import Reviewer
def review_change(reviewer, local_sha):
  upstream_sha = reviewer.get_cherry_pick_sha_from_local_sha(local_sha)
  upstream_patch = reviewer.get_commit_from_sha(upstream_sha)
  local_patch = reviewer.get_commit_from_sha(local_sha)
  result = reviewer.compare_diffs(upstream_patch, local_patch)
  if reviewer.verbose or reviewer.chatty or len(result):
    print('Reviewing %s (rmt=%s)' % (local_sha, upstream_sha[:11]))
  for l in result:
  if len(result):
  return len(result)

  reviewer = Reviewer(args.verbose, args.chatty)
      this_ret = review_change(reviewer, m.group(1))